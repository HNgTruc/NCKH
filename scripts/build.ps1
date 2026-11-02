<#
Ghép các mục thuyết minh (thuyet-minh/00-*.md đến 99-*.md) thành một file Word để cả nhóm đọc duyệt.
Khối hướng dẫn <!-- --> không xuất ra Word. Bản nộp cuối vẫn phải chép vào file mẫu .docx của trường.

Cách chạy, từ thư mục gốc repo:
    ./scripts/build.ps1
    ./scripts/build.ps1 -Out xuat-ban/ban-nhap-2.docx

Nếu PowerShell chặn chạy script:
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
#>
param(
    [string]$Out = "xuat-ban/thuyet-minh-nhap.docx"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Error "Chưa cài pandoc. Cài bằng: winget install --id JohnMacFarlane.Pandoc, rồi mở lại terminal."
}

$files = Get-ChildItem -Path "thuyet-minh" -Filter "*.md" |
    Where-Object { $_.Name -match '^\d' } |
    Sort-Object Name |
    ForEach-Object { $_.FullName }

if ($files.Count -eq 0) {
    Write-Error "Không tìm thấy file mục nào trong thuyet-minh/."
}

$todo = Select-String -Path $files -Pattern '\[TODO|\[CẦN NGUỒN\]|\[TỰ VIẾT LẠI\]' -Encoding utf8
if ($todo) {
    Write-Warning "Còn $($todo.Count) chỗ đánh dấu TODO / CẦN NGUỒN / TỰ VIẾT LẠI. Bản xuất là bản nháp."
}

$outDir = Split-Path -Parent $Out
if ($outDir) { New-Item -ItemType Directory -Force -Path $outDir | Out-Null }

pandoc @files --from markdown --to docx --output $Out
Write-Host "Đã tạo $Out từ $($files.Count) file."
