from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 45)
pdf.cell(0, 60, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=0, y=70)
pdf.set_font_size(30)
pdf.set_text_color(255, 255, 255)
pdf.text(x=45, y=120, txt=f"{name} took CS50", color=(0, 255, 255))
pdf.output("Shirtificate.pdf")

