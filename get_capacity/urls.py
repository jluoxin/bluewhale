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

from django.conf.urls import patterns

urlpatterns = patterns(
    'get_capacity.views',
    (r'^$', 'home'),
    # 表单下拉数据获取及渲染
    (r'^get_biz_list/$', 'get_biz_list'),
    (r'^get_ip_by_bizid/$', 'get_ip_by_bizid'),
    (r'^get_job_list/$', 'get_joblist_by_bizid'),

        # 执行作业，获取容量数据
    (r'^execute_job/$', 'execute_job'),
    (r'^get_capacity/$', 'get_capacity'),

    # 获取视图数据
    (r'^chartdata/$', 'get_capacity_chartdata'),
)
