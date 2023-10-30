import plotly_express as px
from PyQt5.QtGui import QPixmap
import requests
import pandas as pd


class graphGen:
    def generateGraph():
        response = requests.get('http://127.0.0.1:5000/graph/users').json()

        df = pd.DataFrame(response)
        df= df.sort_values(by="dates")
        df.index = df.index.astype(int)
        fig = px.line(df, x="dates", y="count", title='Appointments by Day').update_layout(
                    xaxis_title="Date", yaxis_title="Appointments"
                )
        pixmap = QPixmap()
        return pixmap.loadFromData(fig.to_image(format="png", width=600, height=350, scale=2))
        
    
        """
        plt.plot(df['dates'],df['count'])
        plt.show()"""