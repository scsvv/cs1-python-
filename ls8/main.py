# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         num_set = set()
#         for num in nums:
#             complement = target - num
#             if complement in num_set:
#                 # Нашли пару чисел, сумма которых равна target
#                 first_index = nums.index(complement)
#                 second_index = nums.index(num, first_index + 1)
#                 return [first_index, second_index]
#             num_set.add(num)

import pyautogui
import time

pyautogui.press('win')
time.sleep(1)

pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1)

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Turpis in eu mi bibendum neque egestas congue. Sit amet est placerat in egestas erat. Augue eget arcu dictum varius duis at consectetur. Non arcu risus quis varius quam. Ornare lectus sit amet est placerat in egestas erat. Amet nisl suscipit adipiscing bibendum est ultricies integer quis auctor. Consequat semper viverra nam libero justo laoreet sit amet. Sit amet mattis vulputate enim. Lobortis mattis aliquam faucibus purus in massa tempor nec feugiat.
Euismod lacinia at quis risus. Mauris vitae ultricies leo integer malesuada nunc vel risus. Sapien faucibus et molestie ac feugiat. Eleifend donec pretium vulputate sapien nec sagittis. Duis at consectetur lorem donec massa. Aliquet porttitor lacus luctus accumsan. Mattis enim ut tellus elementum sagittis vitae et leo duis. Volutpat lacus laoreet non curabitur. Duis tristique sollicitudin nibh sit amet. Ut sem nulla pharetra diam sit amet nisl suscipit adipiscing. Pellentesque habitant morbi tristique senectus et. Aliquam id diam maecenas ultricies mi eget mauris. Tellus mauris a diam maecenas sed enim ut sem. Metus dictum at tempor commodo. Ut diam quam nulla porttitor massa. Sem fringilla ut morbi tincidunt augue interdum velit euismod in.
Arcu risus quis varius quam quisque id diam vel quam. Cursus risus at ultrices mi. Senectus et netus et malesuada fames ac. Nulla posuere sollicitudin aliquam ultrices. Cras adipiscing enim eu turpis egestas pretium aenean. Montes nascetur ridiculus mus mauris vitae ultricies. Ut tristique et egestas quis. Volutpat est velit egestas dui id. In nisl nisi scelerisque eu. Tincidunt praesent semper feugiat nibh sed pulvinar. Justo donec enim diam vulputate. Auctor eu augue ut lectus.
Ultrices tincidunt arcu non sodales. Enim facilisis gravida neque convallis a cras. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus non. Blandit massa enim nec dui nunc mattis enim ut. Tellus in hac habitasse platea dictumst vestibulum rhoncus. Sed felis eget velit aliquet. Fames ac turpis egestas integer eget aliquet nibh. Sit amet mauris commodo quis imperdiet massa. Eu lobortis elementum nibh tellus molestie nunc. In cursus turpis massa tincidunt dui ut ornare. Eu facilisis sed odio morbi quis. Ipsum dolor sit amet consectetur adipiscing elit ut. Quis lectus nulla at volutpat diam. Malesuada fames ac turpis egestas sed tempus urna. Odio pellentesque diam volutpat commodo sed egestas egestas fringilla phasellus. Tempor orci dapibus ultrices in iaculis nunc. Urna cursus eget nunc scelerisque.
Tellus mauris a diam maecenas sed enim ut sem. Egestas erat imperdiet sed euismod nisi porta lorem mollis. Sed odio morbi quis commodo odio aenean sed. Sed felis eget velit aliquet sagittis id consectetur purus ut. Facilisi etiam dignissim diam quis enim lobortis. Facilisis volutpat est velit egestas dui id. Diam in arcu cursus euismod. Non pulvinar neque laoreet suspendisse interdum. Est velit egestas dui id ornare arcu odio ut. Eget sit amet tellus cras adipiscing enim eu turpis egestas. Sit amet nulla facilisi morbi tempus iaculis urna id. Nisl suscipit adipiscing bibendum est ultricies integer quis auctor. Egestas purus viverra accumsan in. Laoreet suspendisse interdum consectetur libero id faucibus nisl tincidunt. Ipsum consequat nisl vel pretium. Dictum non consectetur a erat nam.
"""

pyautogui.write(text, interval=0.1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('example.txt')
pyautogui.press('enter')

pyautogui.hotkey('alt', 'f4')
