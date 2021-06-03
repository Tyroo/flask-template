from flask import (Blueprint, request,
                   render_template, current_app, make_response
                   )
from werkzeug.utils import secure_filename

import os

# 实例化一个文件蓝图对象
file_bp = Blueprint('file', __name__, url_prefix='/file')


# 文件上传API
@file_bp.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            return make_response('ERROR')
        file.save(os.path.join(current_app.config.get('FILE_UPLOAD_BASE_PATH'),
                               secure_filename(file.filename)))
        return make_response('OK')
    else:
        return render_template('FileUpload.html')
