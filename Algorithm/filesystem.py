import os
import shutil


class FileSystem:
    def __init__(self, directory_path):
        self.dir = os.path.abspath(directory_path)
        self.dir_list = os.listdir(self.dir)
        # 절대주소 값이 안들어오면 현재 디랙토리 값으로 상대 주소

        self.search_option = [True, True]  # search option [0] : 파일 [1] : 디렉토리
        self.select_list = []

    # 파일/디렉토리 삭제
    def file_delete(self, names):
        if names != "":
            if os.path.isdir(names):
                shutil.rmtree(names)
            if os.path.isfile(names):
                os.remove(names)

    # 파일/디렉토리 복사
    def file_copy(self, names):
        # names [0] : 작업을 시행할 파일/디렉토리 [1] : 복사할 이름
        if not (names[0] == "" or names[1] == ""):
            if os.path.isdir(names):
                shutil.copytree(names[0], names[1])
            if os.path.isfile(names):
                shutil.copy(names[0], names[1])
        else:
            msg = "ERROR : 파일이 선택되지않음"
            # System.error(msg) 나중에 System 전용 클래스 만들어서 할 예정

    # 파일/디렉토리 이동
    def file_move(self, names):
        # names [0] : 이동할 파일/디렉토리 [1] : 이동할 위치
        if not (names[0] == "" or names[1] == ""):
            shutil.move(names[0], names[1])
        else:
            msg = "ERROR : 파일이 선택되지않음"

    # 파일/디렉토리 선택
    def file_select(self, names):
        if names != "" and os.path.exists(names):
            if self.select_list in names:
                self.select_list.remove(names)
            else:
                self.select_list.append(names)

    # 파일/디렉토리 정보
    def file_info(self, names):
        # more update
        return names
