from fpdf import FPDF
"""
- ok The orientation of the PDF should be Portrait.
- ok The format of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
- The shirt’s image should be centered horizontally.
- The user’s name should be on top of the shirt, in white text.
"""
# pdf.cell(w=None, h=None, txt='', border=0, ln='DEPRECATED', align=Align.L, fill=False, link='', center=False, markdown=False, new_x=XPos.RIGHT, new_y=YPos.TOP)

def main():
    name = input("Name: ")
    #print(f"{name} took CS50")
    tag = name + " took CS50"


    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 45)
    pdf.cell(0, 60, "CS50 Shirtificate", align='C', center=True)
    pdf.image("./shirtificate.png", x=0, y=70)
    pdf.set_font_size(30)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=45, y=140, txt=f"{tag}")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

