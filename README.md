# Trabalho - A1 Linguagens de Programação
Bruno Cavalli, Erik Rolin, Nicholas Farrel

## About the project and the data

In this work, we perform data analysis and visualization using the Seaborn and Pandas libraries. The data used comes from the SAEB (Basic Education Assessment System), which offers a wide variety of data on students and their schools.

## Project structure

The project is organized in the following modules:

- `Python_scripts`: Contains the Python scripts used to clean the dataset and create the analyses.
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

   ![Heatmap - Reproval Rate](graphs/heatmap_reprovacao.png)


2. Heatmap - Association between Parents' Responses and Abandonment Rate:
   
   ![Heatmap - Abandonment Rate](graphs/heatmap_abandono.png)


3. Boxplot - Association between number of matriculated students and avarege score:

   ![Boxplot - Students Matriculated](graphs/boxplot_matric.png)

4. Boxplot - Association between students participation and the avarege score:

   ![Boxplot - Student Participation](graphs/boxplot_part.png)

5. Boxplot - Association between region of the school and the avarege score:

   1.0 = Sudeste ; 2.0 =; 3.0=; 4.0=; 5.0=

   ![Boxplot - School Region](graphs/boxplot_regia_media.png)

6. Boxplot - Association between the state location of the scool and the avarege score:

   ![Boxplot - School State](graphs/boxplot_uf_media.png)

7. Heatmap - Association between the region and the socioeconomical level of the school:

   ![Heatmap - Region Socioeconomical](graphs/heatmap_regiao_socio.png)

8. Boxplot - Association between school localization(Interior or Capital) and avarege score:

   ![Boxplot - School Localization](graphs/boxplot_loc.png)

9. Boxplot - Association between the type of school (public or private) and the avarege score:

   ![Boxplot - School Type](graphs/boxplot_tipo.png)