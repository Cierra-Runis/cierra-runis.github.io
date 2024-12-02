# 参数定义块
param (
    [string]$mode
)

# 函数定义
function build_module {
    Write-Host "> 清除旧构建"
    hexo clean

    Write-Host "> 构建中"
    hexo generate

    Write-Host "> 开启服务中"
    hexo server
}

function release_module {
    Write-Host "> 清除旧构建"
    hexo clean

    Write-Host "> 构建中"
    hexo generate

    Write-Host "> 发布中"
    hexo deploy

    Write-Host "> 同步本仓库中"
    git add .
    git commit -m "修改"
    git push --force

    Write-Host "> 已发布携带信息为 '修改' 的仓库, 请检查发布情况"
}

# 主逻辑
if ($mode -eq "--release") {
    release_module
} elseif ($mode -eq "--build") {
    build_module
} else {
    Write-Host "无效的参数，请使用 --release 或 --build"
    exit 1
}
