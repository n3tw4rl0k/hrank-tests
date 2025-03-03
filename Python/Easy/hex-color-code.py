from io import StringIO
import sys

#test case 1
# input_sample = """11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }  """

# # test case 2
# input_sample = """35
# .arrow-up {
# 	width: 0;
# 	height: 0;
# 	border-left: 5px solid transparent;
# 	border-right: 5px solid transparent;
#
# 	border-bottom: 5px solid black;
# }
#
# .arrow-down {
# 	width: 0;
# 	height: 0;
# 	border-left: 20px solid transparent;
# 	border-right: 20px solid transparent;
#
# 	border-top: 20px solid #f00;
# }
#
# .arrow-right {
# 	width: 0;
# 	height: 0;
# 	border-top: 60px solid transparent;
# 	border-bottom: 60px solid transparent;
#
# 	border-left: 60px solid green;
# }
#
# #f0f {
# 	width: 0;
# 	height: 0;
# 	border-top: 10px solid transparent;
# 	border-bottom: 10px solid transparent;
#
# 	border-right:10px solid blue;
# }"""

# test case 3
input_sample = """24
.custom-file-input::-webkit-file-upload-button {
  visibility: hidden;
}
.custom-file-input::before {
  content: 'Select some files';
  display: inline-block;
  background: -webkit-linear-gradient(top, #f9f9f9, #e3e3e3);
  border: 1px solid #999;
  border-radius: 3px;
  padding: 5px 8px;
  outline: none;
  white-space: nowrap;
  -webkit-user-select: none;
  cursor: pointer;
  text-shadow: 1px 1px #fff;
  font-weight: 700;
  font-size: 10pt;
}
.custom-file-input:hover::before {
  border-color: black;
}
.custom-file-input:active::before {
  background: -webkit-linear-gradient(top, #e3e3e3, #f9f9f9);
}"""


sys.stdin = StringIO(input_sample)

import re

input_n = int(input())

color_code_re = "#(.+?)(?=[\s;,)]|$)"

for _ in range(input_n):

    new_line = input()
    code_find = re.findall(color_code_re, new_line)
    if len(code_find) == 1:
        if str("#" + code_find[0]) == new_line:
            continue
        elif new_line[-1] == "{" and new_line[0] == "#":
            continue

    for x in code_find:
        if len(x) != 3 and len(x) != 6:
            continue
        flag = False
        for z in x:
            if z not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F"):
                flag = True
                break
        if not flag:
            print("#"+x)
