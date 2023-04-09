from typing import List


class Solution:
    class Folder:
        def __init__(self, content: List[any] = [], parent=None) -> None:
            self.content = content
            self.parent: self.Folder = parent

        def get_parent(self):
            return self.parent

        def set_parent(self, parent) -> None:
            self.parent = parent

        def set_content(self, content) -> None:
            self.content = content

    def __init__(self, day: int) -> None:
        self.day_number: int = day
        self.topology_dict: dict = {"/": self.Folder()}
        self.current_parent = self.topology_dict["/"]
        self.files_dict: dict = {}
        self.searching_ls = False

    def asign_directory_content(self, parent_folder):
        pass

    def command_switcher(self, command, target, content):
        if command == "cd":
            if self.searching_ls:
                self.searching_ls = False
                print(self.current_parent, type(self.current_parent))
                self.current_parent.set_content(content)
                print(content)
            if ".." != target:
                self.current_parent = target
                return
            self.current_parent = self.current_parent.get_parent()
        ## This is only for the LS command.
        else:
            self.searching_ls = True

    def read_file(self):
        with open(f"inputs/{self.day_number}.txt", "r") as input:
            tmp = []
            for line in input.readlines():
                if "$" in line:
                    try:
                        cmd, trgt = line.split("$")[1].strip().split(" ")
                    except:
                        cmd = line.split("$")[1].strip().split(" ")[0]
                    self.command_switcher(cmd, trgt, tmp)
                if self.searching_ls:
                    tmp.append(line)


sol = Solution(7)
sol.read_file()
print(sol.topology_dict["/"].content)
