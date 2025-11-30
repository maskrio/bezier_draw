def segments_to_pdf_content(segments):
    lines = []
    lines.append("0 0 0 RG")  # stroke color black
    lines.append("1 w")  # line width

    for x1, y1, x2, y2, x3, y3, x4, y4 in segments:
        lines.append(f"{x1} {y1} m")
        lines.append(f"{x2} {y2} {x3} {y3} {x4} {y4} c")

    lines.append("S")
    content = "\n".join(lines) + "\n"
    return content


def calc_size(segments):
    xs = segments[:, 0::2]
    ys = segments[:, 1::2]
    width = xs.max() + xs.min()
    height = ys.max() + ys.min()
    return width, height


def write_to_pdf(segments, filename):
    content_str = segments_to_pdf_content(segments)
    content_bytes = content_str.encode("ascii")
    content_len = len(content_bytes)

    width, height = calc_size(segments)

    header = f"""
    %PDF-1.4
1 0 obj
<< /Type /Catalog
/Outlines 2 0 R
/Pages 3 0 R
>>
endobj
2 0 obj
<< /Type Outlines
/Count 0
>>
endobj
3 0 obj
<< /Type /Pages
/Kids [ 4 0 R ]
/Count 1
>>
endobj

4 0 obj
<< /Type /Page
/Parent 3 0 R
/MediaBox [ 0 0 {width} {height} ]
/Contents 5 0 R
/Resources << /ProcSet 6 0 R >>
>>
endobj
    """.encode(
        "ascii"
    )

    start_content = f"""
5 0 obj
<< /Length {content_len} >>
stream
""".encode(
        "ascii"
    )

    end_content = """
endstream
endobj
""".encode(
        "ascii"
    )

    content = start_content + content_bytes + end_content

    footer = """
xref
0 7
0000000000 65535 f
0000000009 00000 n
0000000074 00000 n
0000000120 00000 n
0000000179 00000 n
0000000300 00000 n
0000000384 00000 n
trailer
<< /Size 7
/Root 1 0 R
>>
startxref
408
%%EOF""".encode(
        "ascii"
    )

    with open(filename, "wb") as f:
        f.write(b"".join([header, content, footer]))
