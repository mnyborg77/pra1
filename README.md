# Práctica 1 - Tipología y Ciclo de Vida de los Datos

Asignatura: M2.851 / Semestre: 20222-2 / Fecha: 20-11-2022

URL del sitio web elegido: [https://www.hm.com/entrance.ahtml](https://www.hm.com/entrance.ahtml)

## Autores

* Morten Nyborg - mnyborg@uoc.edu

## Descripción del repositorio

Hemos elegido extraer información de las páginas H&M en Europa. Todas las páginas tienen una estructura muy parecida y pensamos que podemos extraer los datos que nos interesan de distintas páginas usando pocos patrones. El sitio web que nos da acceso a todas las páginas de los mercados de la marce es https://www.hm.com/entrance.ahtml. Las páginas de los mercados son páginas de comercio electrónico html, que contienen información sobre los productos de la marca y sus precios.

El resultado de realizar el web scraping es el repositorio TCVD-PRACTICA1, con sus contenidos principales el algoritmo para hacer el web scraping, el resultado en forma de csv, la memoria.

* memoria.pdf: Documento que explica en detalle el trabajo, incluye el origen de los datos y su propietario, la motivación para realizarlo, el proceso seguido para obtener los datos.
* /dataset/hm_offers.csv: Resultado de realizar el web scraping
* /source: código usado para realizar el web scraping
* /source/hmscraper/hmscraper/spiders/hm_spider.py: Archivo principal.
* /source/hmscraper/hmscraper/setting.py
* /source/hmscraper/hmscraper/items.py
* /source/hmscraper/hmscraper/middlewares.py
* /source/hmscraper/hmscraper/pipelines.py
* /source/requirements.txt: Lista de paquetes utilizados. (python 3.10).

## Ejecución

El scraper se debe ejecutar de la siguiente manera:

cd al directorio source/requirements.txt
activa tu virtualenv y ejecuta en el shell:

```
pip install -r requirements.txt

cd source/hmscraper/hmscraper

scrapy crawl hm -o absolute_path/hm_offers.csv
```

Absolute_path es el path absoluto donde quieras guardar el dataset.

## Publicación en Zenodo

El dataset ha sido publicado en Zenodo con DOI [10.5281/zenodo.7338342](https://doi.org/10.5281/zenodo.7338342).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7338342.svg)](https://doi.org/10.5281/zenodo.7338342)

## Vídeo de presentación
