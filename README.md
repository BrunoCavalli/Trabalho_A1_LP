# Trabalho - A1 Linguagens de Programação
Bruno Cavalli, Erik Rolin, Nicholas Farrel

## About the project and the data

In this project, we perform data analysis and visualization using the Seaborn and Pandas libraries. The data used comes from the SAEB (Basic Education Assessment System), which offers a wide variety of data on students and their schools.

Since the original dataset was quite large, we have already performed data cleaning and removed the raw file from this repository. However, you can access the original dataset through the [open data portal](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb) provided by the Brazilian government.

### Steps to Download and Prepare the Data

1. **Download the Dataset**:
   - Visit the [SAEB open data portal](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb) and download the `microdados_saeb_2021.zip` file.

2. **Extract the Files**:
   - Extract the contents of the zip file to your local machine.

3. **Place the Required Files**:
   - From the extracted folder, locate the following files:
     - `TS_ALUNO_34EM.csv`
     - `TS_ESCOLA.csv`
   - Move these two files into the `Data` folder in your project directory.

4. **Run the Data Cleaning Script**:
   - Once the files are in the `Data` folder, run the `Data_cleaning.py` script to clean and preprocess the data.

   ```bash
   python Data_cleaning.py
   ````

## Project structure

The project is organized in the following modules:

- `Python_scripts`: Contains the Python scripts used to clean the dataset and create the analyses.
- `Tests`: Contains all the python scripts used to test the modules
- `Data`: Contains the dataset `.csv` file.

## Getting started

### Prerequisites

To install the required packages, run the following command:

```bash
pip install -r requirements.txt 
````

## Generating Visualizations

To create the generations, you have to run the `main.py` file

````bash
python main.py
````

This will generate the following visualizations:

1. Heatmap - Association between Parents' Responses and Reproval Rate:

   ![Heatmap - Reproval Rate](Graphs/heatmap_reprovacao.png)


2. Heatmap - Association between Parents' Responses and Abandonment Rate:
   
   ![Heatmap - Abandonment Rate](Graphs/heatmap_abandono.png)


3. Boxplot - Association between number of matriculated students and avarege score:

   ![Boxplot - Students Matriculated](Graphs/boxplot_matric.png)

4. Boxplot - Association between students participation and the avarege score:

   ![Boxplot - Student Participation](Graphs/boxplot_part.png)

5. Boxplot - Association between region of the school and the avarege score:

### Region Legend

- 1 = Norte 
- 2 = Nordeste 
- 3 = Sudeste 
- 4 = Sul
- 5 = Centro-Oeste

   ![Boxplot - School Region](Graphs/boxplot_regia_media.png)

6. Boxplot - Association between the state location of the scool and the avarege score:

### State Code Legend

- 11 = RO (Rondônia)
- 12 = AC (Acre)
- 13 = AM (Amazonas)
- 14 = RR (Roraima)
- 15 = PA (Pará)
- 16 = AP (Amapá)
- 17 = TO (Tocantins)
- 21 = MA (Maranhão)
- 22 = PI (Piauí)
- 23 = CE (Ceará)
- 24 = RN (Rio Grande do Norte)
- 25 = PB (Paraíba)
- 26 = PE (Pernambuco)
- 27 = AL (Alagoas)
- 28 = SE (Sergipe)
- 29 = BA (Bahia)
- 31 = MG (Minas Gerais)
- 32 = ES (Espírito Santo)
- 33 = RJ (Rio de Janeiro)
- 35 = SP (São Paulo)
- 41 = PR (Paraná)
- 42 = SC (Santa Catarina)
- 43 = RS (Rio Grande do Sul)
- 50 = MS (Mato Grosso do Sul)
- 51 = MT (Mato Grosso)
- 52 = GO (Goiás)
- 53 = DF (Distrito Federal)


   ![Boxplot - School State](Graphs/boxplot_uf_media.png)

7. Heatmap - Association between the region and the socioeconomical level of the school:

   ![Heatmap - Region Socioeconomical](Graphs/heatmap_regiao_socio.png)

8. Boxplot - Association between school localization(Interior or Capital) and avarege score:

   - 1 = Urbana
   - 2 = Rural

   ![Boxplot - School Localization](Graphs/boxplot_loc.png)

9. Boxplot - Association between the type of school (public or private) and the avarege score:

   - A = Only Public School
   - B = Only Private School
   - C = Both Private and Public


   ![Boxplot - School Type](Graphs/boxplot_tipo.png)


## Testing the modules

To test the modules, run:
````bash
pytest
````

If you want to run the test of an individual module, run:
````bash
pytest <file-name.py>
````