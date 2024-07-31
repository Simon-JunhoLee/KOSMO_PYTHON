from flask import Blueprint, render_template, request
from dao import bbsDAO
import json

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('/')
def list():
    return render_template('index.html', title='게시판', pageName='bbs/list.html')

@bp.route('/list.json')
def listJSON():
    return bbsDAO.list()

@bp.route('/insert')
def insert():
    return render_template('index.html', title='글쓰기', pageName='bbs/insert.html')

@bp.route('/insert', methods=['POST'])
def insertPost():
    req = json.loads(request.get_data())
    result = bbsDAO.insert(req)
    return result

@bp.route('/<int:bid>')
def read(bid):
    vo = bbsDAO.read(bid)
    return render_template('index.html', title='게시글 정보', pageName='bbs/read.html', bbs=vo)

@bp.route('/<int:bid>', methods=['DELETE'])
def delete(bid):
    result = bbsDAO.delete(bid)
    return result

