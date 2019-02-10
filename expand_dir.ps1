function Expand-Dir ($From, $To) {
    <# 将一个拥有多层目录的文件夹中的所有文件移动到目标文件夹 #>
    $From = (Resolve-Path $From)
    $To = (Resolve-Path $To)
    foreach ($obj in (Get-ChildItem $From)){
        if ($obj -is [IO.FileInfo]){        # 复制文件, 如果重名, 则添加一串 MD5 Hash
            try {
                Move-Item -Path $From\$obj -Destination $To
                Write-Verbose "move $From\$obj to $To\$obj"
            }
            catch {
                $insert_name = (Get-FileHash -Algorithm md5 $obj)
                $base_name = $obj.BaseName
                $ext_name = $obj.Extension
                $new_name = "$base_name.$insert_name$ext_name"
                Move-Item -Path $From\$obj -Destination "$To\$new_name"
                Write-Verbose "move $From\$obj to $To\$new_name"
            }
        } elseif ($obj -is [IO.DirectoryInfo]) {        # 递归目录, 删除目录
            Write-Verbose ">>> $From\$obj is a Dir, enter"
            Expand-Dir -From $From\$obj -To $To
            Remove-Item $From\$obj
        } else {
            Write-Error $obj.GetType().Name           # 出现问题, 自己看
            Write-Error "!!! $From\$obj is not a file or dir"
        }
    }
}