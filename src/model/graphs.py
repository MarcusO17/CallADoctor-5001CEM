import plotly_express as px
from PyQt5.QtGui import QPixmap
import requests
import io
from PIL import Image
import pandas as pd


class graphGen:
    def generateGraph():
        response = requests.get('http://127.0.0.1:5000/graph/users').json()

        if len(response) == 0:
            return None

        df = pd.DataFrame(response)
        df= df.sort_values(by="dates")
        df.index = df.index.astype(int)
        fig = px.line(df, x="dates", y="count", title='Appointments by Day').update_layout(
                    xaxis_title="Date", yaxis_title="Appointments"
                )
        figBytes = fig.to_image(format="png", width=600, height=350, scale=1)
        return Image.open(io.BytesIO(figBytes))
    
        
    
        """
        plt.plot(df['dates'],df['count'])
        plt.show()"""