def calculate(number1, operation, number2):
    if operation == "+":
        result = int(number1) + int(number2)
    elif operation == "-":
        result = int(number1) - int(number2)
    return result


def prettyprint(text, length):
    spaces = ""
    for _ in range(0, length - len(text)):
        spaces += " "
    formatted_text = spaces + text
    return formatted_text


def arrange(term1, term2, op):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    if len(term1) > len(term2):
        term2 = prettyprint(term2, len(term1))
    else:
        term1 = prettyprint(term1, len(term2))

    line1 = "  " + term1
    line2 = op + " " + term2

    for _ in range(0, len(line2)):
        line3 += "-"

    result = calculate(term1, op, term2)

    line4 = prettyprint(str(result), len(line3))

    return [line1, line2, line3, line4]


def arithmetic_arranger(problems, *args):
    show_solution = False

    if True in args:
        show_solution = True

    if len(problems) > 5:
        return "Error: Too many problems."

    results = []

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        terms = problem.split(" ")
        term1 = terms[0]
        op = terms[1]
        term2 = terms[2]

        try:
            int(term1)
            int(term2)
        except ValueError:
            return "Error: Numbers must only contain digits."

        if op not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        if len(term1) > 4 or len(term2) > 4:
            return "Error: Numbers cannot be more than four digits."

        results.append(arrange(term1, term2, op))

    for i in range(0, len(results) - 1):
        line1 += results[i][0] + "    "
        line2 += results[i][1] + "    "
        line3 += results[i][2] + "    "
        line4 += results[i][3] + "    "

    line1 += results[len(results) - 1][0]
    line2 += results[len(results) - 1][1]
    line3 += results[len(results) - 1][2]
    line4 += results[len(results) - 1][3]

    if show_solution:
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
        return line1 + "\n" + line2 + "\n" + line3
