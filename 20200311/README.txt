# Cuando comenzamos un proyecto primero crear un entorno de trabajo

````
$ conda create -n pep python=3 
````
o usar virtualenv.

# Activar el entorno
````
$ conda activate pep
````

# Instalar librerias a usar.
````
$ conda install pandas
````
# listar las librerias
````
$ conda list
````

````
$ pip install jupyterlab
$ pip install matplotlib
$ pip install scikit-learn
````

y despues que esta todo instalado podemos correr jupiter-lab

````
(pep) [j3nnn1@itup ~]$ whereis jupyter-lab
jupyter-lab: /home/j3nnn1/anaconda3/envs/pep/bin/jupyter-lab
(pep) [j3nnn1@itup ~]$ jupyter-lab
[I 2021-03-11 19:58:18.721 ServerApp] jupyterlab | extension was successfully linked.
[I 2021-03-11 19:58:18.737 ServerApp] Writing notebook server cookie secret to /home/j3nnn1/.local/share/jupyter/runtime/jupyter_cookie_secret
````
