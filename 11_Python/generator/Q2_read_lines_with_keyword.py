# Q2. 實作一個 generator，逐行讀取大型檔案，只 yield 包含 keyword 的行
# 不能一次把整個檔案載入記憶體

from typing import Generator


def read_lines_with_keyword(filepath: str, keyword: str) -> Generator[str, None, None]:
    with open(filepath) as f:
        for line in f:
            if keyword in line:
                yield line.rstrip("\n")


if __name__ == "__main__":
    import os
    import tempfile

    with tempfile.NamedTemporaryFile("w", suffix=".log", delete=False) as f:
        f.write("INFO start\nERROR something failed\nINFO ok\nERROR timeout\n")
        path = f.name

    result = list(read_lines_with_keyword(path, "ERROR"))
    assert result == ["ERROR something failed", "ERROR timeout"]
    os.unlink(path)
    print("passed")
