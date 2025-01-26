from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

# 合并单元格
def merge_in_col(excel_file, column_name, sheet_name=None, exclude_header=True):
    wb = load_workbook(excel_file)
    if sheet_name:
        ws = wb[sheet_name]
    else:
        ws = wb.active

    header = [cell.value for cell in ws[1]]
    column_index = header.index(column_name) + 1
    column_letter = get_column_letter(column_index)

    start_row = 2 if exclude_header else 1
    merge_value = None
    merge_start = start_row

    for row in range(start_row, ws.max_row+1):
        cell_value = ws[f'{column_letter}{row}'].value
        if cell_value == merge_value:
            continue
        else:
            if row - merge_start > 1:
                ws.merge_cells(f'{column_letter}{merge_start}:{column_letter}{row-1}')
            merge_start = row
            merge_value = cell_value

    # 处理最后一组合并
    if ws.max_row - merge_start > 0:
        ws.merge_cells(f'{column_letter}{merge_start}:{column_letter}{ws.max_row}')

    wb.save(excel_file)

# 设置单元格样式
def style_in_col(excel_file, column_name, font_name='黑体', font_size=10, font_color="000000", bg_color=None,
                 condition=lambda value:True, sheet_name=None, exclude_header=True):
    wb = load_workbook(excel_file)
    if sheet_name:
        ws = wb[sheet_name]
    else:
        ws = wb.active

    header = [cell.value for cell in ws[1]]
    column_index = header.index(column_name) + 1
    start_row = 2 if exclude_header else 1

    font = Font(name=font_name, size=font_size, color=font_color)
    fill = PatternFill(fill_type='solid', fgColor=bg_color) if bg_color else PatternFill(fill_type='none')
    for row in ws.iter_rows(min_row=start_row, min_col=column_index, max_col=column_index):
        for cell in row:
            try:
                value = cell.value
                if condition(value):
                    cell.font = font
                    cell.fill = fill
            except:
                continue

    wb.save(excel_file)

def format_in_col(excel_file, column_name, format="0.00", sheet_name=None, exclude_header=True):
    wb = load_workbook(excel_file)
    if sheet_name:
        ws = wb[sheet_name]
    else:
        ws = wb.active

    header = [cell.value for cell in ws[1]]
    column_index = header.index(column_name) + 1
    start_row = 2 if exclude_header else 1

    for row in ws.iter_rows(min_row=start_row, min_col=column_index, max_col=column_index):
        for cell in row:
            cell.number_format = format

    wb.save(excel_file)

def style_header(excel_file, font_name='黑体', font_size=14, sheet_name=None):
    wb = load_workbook(excel_file)
    if sheet_name:
        ws = wb[sheet_name]
    else:
        ws = wb.active

    font = Font(name=font_name, size=font_size, bold=True)
    for cell in ws[1]:
        cell.font = font

    wb.save(excel_file)


