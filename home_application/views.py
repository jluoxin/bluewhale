# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context
from blueking.component.shortcuts import get_client_by_request
from home_application.celery_tasks import async_task, execute_task, get_time

def home(request):
    """
    首页
    """
    # return render_mako_context(request, '/home_application/home.html')

    # 调用自己开发的API组件
    client = get_client_by_request(request)
    kwargs = {'token': '@adf*adsd^'}
    resp = client.cm.get_capacity(**kwargs)
    
    # 执行celery异步任务
    async_task.delay(1, 2, 1)

    # 执行定时任务
    execute_task(2)
    return render_mako_context(request, '/home_application/home.html', {'result': resp})


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def helloworld(request):
    """
    helloworld
    """
    return render_mako_context(request,'/home_application/helloworld.html')