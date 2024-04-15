class Paper:
    def __init__(self, ut, py, so, sn, di, issue, volume, ab=None, ti=None, authors=None, affiliations=None, references=None):
        self.ut = ut
        self.py = py
        self.so = so
        self.sn = sn
        self.di = di
        self.issue = issue
        self.volume = volume
        self.ab = ab
        self.ti = ti
        self.authors = authors if authors else []
        self.affiliations = affiliations if affiliations else []
        self.references = references if references else []

    def add_author(self, author):
        self.authors.append(author)

    def add_affiliation(self, affiliation):
        self.affiliations.append(affiliation)

    def add_reference(self, reference):
        self.references.append(reference)

    def to_txt(self, filename):
        with open(filename, 'a') as file:
            file.write(f"UT: {self.ut}\n")
            file.write(f"PY: {self.py}\n")
            file.write(f"SO: {self.so}\n")
            file.write(f"SN: {self.sn}\n")
            file.write(f"DI: {self.di}\n")
            file.write(f"Issue: {self.issue}\n")
            file.write(f"Volume: {self.volume}\n")
            if self.ab:
                file.write(f"AB: {self.ab}\n")
            if self.ti:
                file.write(f"TI: {self.ti}\n")
            for author in self.authors:
                file.write(f"AU: {author}\n")
            for affiliation in self.affiliations:
                file.write(f"AF: {affiliation}\n")
            for reference in self.references:
                file.write(f"CR: {reference}\n")
            file.write("\n")


def parse_input_file(input_file):
    papers = []
    current_paper = None

    with open(input_file, 'r') as file:
        for line in file:
            if line.strip() == "":
                if current_paper:
                    papers.append(current_paper)
                    current_paper = None
            else:
                tag, value = line.strip().split(": ", 1)
                if tag == "UT":
                    if current_paper:
                        papers.append(current_paper)
                    current_paper = Paper(ut=value)
                elif tag == "PY":
                    current_paper.py = value
                elif tag == "SO":
                    current_paper.so = value
                elif tag == "SN":
                    current_paper.sn = value
                elif tag == "DI":
                    current_paper.di = value
                elif tag == "Issue":
                    current_paper.issue = value
                elif tag == "Volume":
                    current_paper.volume = value
                elif tag == "AB":
                    current_paper.ab = value
                elif tag == "TI":
                    current_paper.ti = value
                elif tag == "AU":
                    current_paper.add_author(value)
                elif tag == "AF":
                    current_paper.add_affiliation(value)
                elif tag == "CR":
                    current_paper.add_reference(value)

    if current_paper:
        papers.append(current_paper)

    return papers

def write_papers_to_txt(papers, output_file):
    for paper in papers:
        paper.to_txt(output_file)

if __name__ == "__main__":
    input_file = "qje2014_2023.txt"
    output_file = "papers_output.txt"
    papers = parse_input_file(input_file)
    write_papers_to_txt(papers, output_file)
