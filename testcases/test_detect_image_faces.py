#!/usr/bin/env python
# coding=utf-8
import pytest
import allure
from testcases.conftest import api_data
from common.logger import logger

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkimm.request.v20170906.DetectImageFacesRequest import DetectImageFacesRequest


@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature("获取图片人脸信息模块")
class TestDetectImageFaces():
    """人脸检测分析模块"""

    @allure.story("用例--获取不同格式图片人脸信息")
    @allure.description("该用例是针对获取不同格式图片人脸信息接口的测试")
    @pytest.mark.parametrize("project, imageuri, expect_status_code, expect_requestid, expect_facemsg, expect_imageurl",
                             api_data["test_detect_image_faces_success"])
    def test_detect_image_faces_success(self, project, imageuri, expect_status_code, expect_requestid, expect_facemsg, expect_imageurl):
        logger.info("*************** 开始执行用例 ***************")

        client = AcsClient('LTAI4G1ZX1dQpM7ZuhZrYHtr', 'nNeLvoE5F2xbSzUslVpesK5JUCtH3a', 'cn-shanghai')

        request = DetectImageFacesRequest()
        request.set_accept_format('json')
        request.set_ImageUri(imageuri)
        request.set_Project(project)
        print("图片路径："+imageuri)

        # try:
        #     response = client.do_action_with_exception(request)
        #     print(str(response, encoding='utf-8'))
        #     res = eval(str(response, encoding='utf-8'))
        #     print(type(res))
        #     assert len(res["RequestId"]) != 0
        #     assert len(res["Faces"]) != 0
        #     assert res["ImageUri"] == expect_imageurl
        # except ServerException as e:
        #     print(e)
        # except ClientException as e:
        #     print(e)

        response = client.do_action_with_exception(request)
        print(type(response))
        print(str(response, encoding='utf-8'))
        res = eval(str(response, encoding='utf-8'))
        print(type(res))
        assert len(res["RequestId"]) != 0
        assert len(res["Faces"]) != 0
        assert res["ImageUri"] == expect_imageurl
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--获取图片人脸信息异常场景的检查")
    @allure.description("该用例是针对获取图片人脸信息异常场景的接口的测试")
    @pytest.mark.parametrize("project, imageuri, expect_status_code, expect_requestid, expect_hostid, expect_code, expect_message, expect_recommend",
                             api_data["test_detect_image_faces_fail"])
    def test_detect_image_faces_fail(self, project, imageuri, expect_status_code, expect_requestid, expect_hostid, expect_code, expect_message, expect_recommend):
        logger.info("*************** 开始执行用例 ***************")
        # global response1
        client = AcsClient('LTAI4G1ZX1dQpM7ZuhZrYHtr', 'nNeLvoE5F2xbSzUslVpesK5JUCtH3a', 'cn-shanghai')

        request = DetectImageFacesRequest()
        request.set_accept_format('json')
        request.set_ImageUri(imageuri)
        request.set_Project(project)
        print("图片路径：" + imageuri)

        # try:
        #     response = client.do_action_with_exception(request)
        #     print(str(response, encoding='utf-8'))
        #     res = eval(str(response, encoding='utf-8'))
        #     print(type(res))
        #     assert len(res["RequestId"]) != 0
        #     assert res["HostId"] == expect_hostid
        #     assert res["Code"] == expect_code
        #     assert res["Message"] == expect_message
        #     assert res["Recommend"] == expect_recommend
        # except ServerException as e:
        #     print(e)
        # except ClientException as e:
        #     print(e)

        response = client.do_action_with_exception(request)
        print(type(response))
        print(str(response, encoding='utf-8'))
        res = eval(str(response, encoding='utf-8'))
        print(type(res))
        assert len(res["RequestId"]) != 0
        assert res["HostId"] == expect_hostid
        assert res["Code"] == expect_code
        assert res["Message"] == expect_message
        assert res["Recommend"] == expect_recommend
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_detect_image_faces.py"])
