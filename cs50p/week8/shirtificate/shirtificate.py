from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="", size=50)
pdf.set_y(30)
pdf.cell(0, 10, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", 10, 70, 190)
pdf.set_text_color(255, 255, 255)
pdf.set_font("helvetica", style="", size=22)
pdf.set_y(130)
pdf.cell(0, 10, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")