from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL do exoPlanetas da Nasa
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# WebDriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(1)  # 10

scarped_data = []

# Defina um método de coleta de dados do exoPlanetas


def scrape():
    print("scrape called!")

    soup = BeautifulSoup(browser.page_source, "html.parser")

    # MUITO IMPORTANTE: A classe "wikitable" e os dados <tr> sáo os existentes no momento da criaCâo deste
    # código.
    # Isso pode ser atualizado no futuro, pois a página é atualizada pela Wikipedia.
    # Entenda a estrutura da página conrorme discutido na aula e execute a coleta de dados do zero.

    # Localize <table>
    # "table", attrs={"class" "wikitable"})
    bright_star_table = soup.find("tbody")

    # Localize <body>
    # table_body = bright_star_table.find_all('tbody')
    # print("table_body", table_body)

    # Localize <tr>
    table_rows = bright_star_table.find_all("tr")  # table_body.find_all('tr')

    # Obenha os dados de ctd>
    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)

        temp_list = []

        for col_data in table_cols:
            # Imprima somente colunas de dados textuais usando a propriedade ".text"

            # Remova os espaCos em branco extras usando o método strip()
            data = col_data.text.strip()
            print("data:", data)

            temp_list.append(data)

        # Anexe os dados à lista star_data
        scarped_data.append(temp_list)


# Chamando o Método
scrape()

stars_data = []

for i in range(0, len(scarped_data)):
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][4]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

# Defina o cabeçalho
headers = ["name", "distance(ly)",
           "mass", "radius", "luminosity"]
# Star_name, Distance, Mass, Radius, Luminosity

# Defina o dataframe do Pandas
star_df_1 = pd.DataFrame(stars_data, columns=headers)

print("stars_data:", stars_data)

# Converta para CSV
star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")
