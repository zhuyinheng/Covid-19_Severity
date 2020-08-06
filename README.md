# Code and dataset of *A Learning-based Model to Evaluate Hospitalization Priority in COVID-19 Pandemics*

[Paper](https://www.cell.com/patterns/fulltext/S2666-3899(20)30120-3)

***if you find it difficult to deploy/use/reproduce/modify it, feel free to start an issue or contact me: zhuyh19 AT mails.tsinghua.edu.cn.***

If you are a hospital worker and want to use the method proposed in this paper, we develop a simple and easy-to-used tool [here](http://covid-19.zyh.science:8888/).

If you want to reprocedure the result or use this code for other purpose, please follow the instructions below.

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

## reproduction

### jupyter
1. start jupyter `jupyter notebook --ip=0.0.0.0 --port=8888`
2. open brower and goto:`localhost:8888/notebooks/Reproduction.ipynb#`
3. run all
4. results are shown in the web notebook and saved to `./paper` folder at the same time

### convert generate png figures to pdf
```
ls -1 *.png | xargs -n 1 bash -c 'convert "$0" "${0%.*}.pdf"'
```
### start web application

1. `flask run --host=0.0.0.0 --port=8889`
2. open brower and goto:`localhost:8889`

## citation
```
@article{Zheng2020ALM,
  title={A Learning-based Model to Evaluate Hospitalization Priority in COVID-19 Pandemics},
  author={Yichao Zheng and Yinheng Zhu and Mengqi Ji and Rongpin Wang and Xinfeng Liu and Mudan Zhang and Choo Hui Qin and Lu Fang and Shao-hua Ma},
  journal={Patterns (New York, N.y.)},
  year={2020}
}
```
