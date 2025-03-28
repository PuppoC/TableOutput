from flask import Flask
import pandas as pd

app = Flask(__name__)

# Load the table
df = pd.read_csv("Table_Input.csv")

def getABC(df):
    alpha = int(df.at[4, 'Value'] + df.at[19, 'Value'])
    beta = int(df.at[14, 'Value'] / df.at[6, 'Value'])  # assume no zero division
    charlie = int(df.at[12, 'Value'] * df.at[11, 'Value'])
    return alpha, beta, charlie

@app.route("/")
def index():
    alpha, beta, charlie = getABC(df)

    style = """
    <style>
        h1 {
            text-align: center;
        }
        table {
            margin: auto;
            border-collapse: collapse;
            width: 20%;
        }
        th, td {
            border: 1px solid;
        }

        
        /* Table 1 */
        .table1 th {
            font-weight: normal;
            text-align: left;
        }
        .table1 td:first-child {
            text-align: left;
        }
        .table1 td:last-child {
            text-align: right;
        }

        
         /* Table 2 */
        .table2 th {
            font-weight: bold;
            text-align: center;
        }
        .table2 td {
            text-align: center;
        }
 
    </style>
    """

    table1HTML = df.to_html(index=False, classes="table1")

    table2HTML = f"""
    <table class='table2'>
        <tr><th>Category</th><th>Value</th></tr>
        <tr><td>Alpha</td><td>{alpha}</td></tr>
        <tr><td>Beta</td><td>{beta}</td></tr>
        <tr><td>Charlie</td><td>{charlie}</td></tr>
    </table>
    """

    return f"{style}<h1>Table 1</h1>{table1HTML}<h1>Table 2</h1>{table2HTML}"

if __name__ == "__main__":
    app.run(debug=True)
