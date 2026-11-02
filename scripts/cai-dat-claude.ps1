<#
Chuyển skills, agents và settings.json từ _claude-setup/ vào .claude/.
Chạy MỘT LẦN sau khi nhận repo, từ thư mục gốc:
    ./scripts/cai-dat-claude.ps1
Sau đó commit thư mục .claude/ để cả nhóm có cùng cấu hình.
Nếu PowerShell chặn chạy script:
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
#>
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$src = Join-Path $root "_claude-setup"
$dst = Join-Path $root ".claude"

if (-not (Test-Path $src)) {
    Write-Host "Không thấy _claude-setup/. Có thể đã cài rồi, kiểm tra thư mục .claude/."
    exit 0
}

$files = Get-ChildItem -Path $src -Recurse -File
foreach ($f in $files) {
    $rel = $f.FullName.Substring($src.Length + 1)
    $target = Join-Path $dst $rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
    Copy-Item -Path $f.FullName -Destination $target -Force
    Write-Host "  .claude\$rel"
}

Remove-Item -Recurse -Force $src
Write-Host "Đã cài $($files.Count) file vào .claude/ và xóa _claude-setup/."
Write-Host "Mở lại Claude Code trong thư mục này để nạp skills và agents."
