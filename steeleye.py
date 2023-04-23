import xml.etree.ElementTree as ET
import pandas as pd

# parse the XML document
tree = ET.parse('data.xml')
root = tree.getroot()

cols = ['FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm', 'FinInstrmGnlAttrbts.ClssfctnTp', 'FinInstrmGnlAttrbts.CmmdtyDerivInd', 'FinInstrmGnlAttrbts.NtnlCcy', 'Issr']
rows = []

# iterate over all TermntdRcrd elements
for termntd_rcrd in root.findall('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}TermntdRcrd'):

    # get the Id, FullNm, and Issr elements
    id_elem = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Id')
    fullnm_elem = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FullNm')
    clssTp = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}ClssfctnTp')
    Cmmdty = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}CmmdtyDerivInd')
    Ntnlccy = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}NtnlCcy')
    issr_elem = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Issr')


    # push the text content of the elements
    rows.append({"FinInstrmGnlAttrbts.Id": id_elem.text,
    				"FinInstrmGnlAttrbts.FullNm": fullnm_elem.text,
    				"FinInstrmGnlAttrbts.ClssfctnTp": clssTp.text,
                    "FinInstrmGnlAttrbts.CmmdtyDerivInd":Cmmdty.text,
                    "FinInstrmGnlAttrbts.NtnlCcy":Ntnlccy.text,
                    "Issr":issr_elem.text
    				})


df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output_final.csv')


