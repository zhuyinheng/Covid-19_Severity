## requirement and environment
1. python 3
2. tested on ubuntu 18. it should work well on win and osx.
```
pip install shap==0.32.1 xgboost==0.90 tensorboardx tensorboard Flask gunicorn matplotlib jupyter seaborn graphviz
```

## file structure
```
- <Root>
    - dataset.csv: released dataset
    - Reproduction.ipynb: reproduction jupyter notebook
    - paper: folder to save reproduction figures and tables
    - tmp: folder to save reproduction intermediate result
    - tsne_point_cloud.json: since t-SNE is interactive, the frozen parameters are provided individually
    - app.py: web app based on flask to provide perdition service
    - Procfile: web app config
    - deploy: folder to save trained model for web app deployment.
    - figures.zip: generated figures and videos
```

## Reproduction

### jupyter
1. start jupyter `jupyter notebook --ip=0.0.0.0 --port=8888`
2. open brower and goto:`localhost:8888/notebooks/Reproduction.ipynb#`
3. run all
4. results are shown in the web notebook and saved to `./paper` folder at the same time
5. 

### convert generate png figures to pdf
```
ls -1 *.png | xargs -n 1 bash -c 'convert "$0" "${0%.*}.pdf"'
```
### start web application

1. `flask run --host=0.0.0.0 --port=8889`
2. open brower and goto:`localhost:8889`

