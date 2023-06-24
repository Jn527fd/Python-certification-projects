import re


def arithmetic_arranger(problems, answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  first_row = ''
  second_row = ''
  third_row = ''
  last_row = ''
  space = ' '
  spacer = space * 4
  line = "-"

  for num in problems:
    figs = re.match(r'([\w\s]+)\s*([\+\-])\s*([\w\s]+)', num)

    if not figs:
      return "Error: Operator must be '+' or '-'."

    left_num = figs.group(1).strip()
    operant = figs.group(2).strip()
    right_num = figs.group(3).strip()

    if not left_num.isdigit() or not right_num.isdigit():
      return "Error: Numbers must only contain digits."

    if len(left_num) > 4 or len(right_num) > 4:
      return "Error: Numbers cannot be more than four digits."

    if len(left_num) > len(right_num):
      line_length = len(left_num) + 2
      space1 = space * (line_length - len(left_num))
      space2 = space * (line_length - (len(right_num) + 1))

      first_row += space1 + left_num + spacer
      second_row += operant + space2 + right_num + spacer
      third_row += line * line_length + spacer

      if answers:
        res = str(eval(num))
        space3 = space * (line_length - len(res))
        last_row += space3 + res + spacer

    else:
      line_length = len(right_num) + 2
      space1 = space * (line_length - len(left_num))
      space2 = space * (line_length - (len(right_num) + 1))

      first_row += space1 + left_num + spacer
      second_row += operant + space2 + right_num + spacer
      third_row += line * line_length + spacer

      if answers:
        res = str(eval(num))
        space3 = space * (line_length - len(res))
        last_row += space3 + res + spacer

  if answers:
    arranged_problems = first_row.rstrip() + '\n' + second_row.rstrip(
    ) + '\n' + third_row.rstrip() + '\n' + last_row.rstrip()
  else:
    arranged_problems = first_row.rstrip() + '\n' + second_row.rstrip(
    ) + '\n' + third_row.rstrip()

  return arranged_problems
