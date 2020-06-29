# -*- coding: utf-8 -*-
# from .baseapi import BaseAPI, PUT, DELETE, POST, GET
# from .baseapi import BaseAPI
# from .utils import list_to_dataframe


#     def get_cell_logs(self, sn, return_type="json", **kwargs):
#         """Return a list of cellular logs for device SN.

#         Parameters
#         ----------
#         sn: string, required
#             The device SN you would like data for
#         return_type: string, required
#             Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
#         params: dict, optional
#             Query based on any column or parameter - see utils for further discussion.

#         Returns
#         -------
#         list or dataframe

#         Examples
#         --------

#         """
#         assert(return_type in ("json", "dataframe")), "Bad return_type"

#         data = self.fetch_data("meta-data/cell-data/{}/".format(sn), **kwargs)
#         if return_type == "dataframe":
#             data = list_to_dataframe(data)
#         return data

#     def add_calibration_model(self, **kwargs):
#         """Add a new calibration model.

#         Parameters
#         ----------
#         params: dict, required
#             A dictionary containing the relevant model upload information including
#             the `sn`, `uploaded`, `name`, `comments`, `object_name`, `training_file`, 
#             `param`, `metrics`, `model_params`, `tag`, and `name`.

#         Returns
#         -------
#         model: dict
#             A dictionary containing the model information that was uploaded.

#         Examples
#         --------
#         >>> api = quantaq.legacy.QuantAQ()
#         >>> api.add_calibration_model(params=dict())

#         """
#         return self._make_request("calibration-models/", type=POST, **kwargs)
    
#     def get_calibration_models(self, sn, **kwargs):
#         """Return the calibration model information for a given device.

#         Parameters
#         ----------
#         sn: string, required
#             The device serial number.

#         Returns
#         -------
#         info: dict
#             A dictionary containing calibration meta information for all models.

#         Examples
#         --------
#         >>> api = quantaq.legacy.QuantAQ()
#         >>> api.get_calibration_models(sn="SN000-001")

#         """
#         return self.fetch_data("calibration-models/{}".format(sn), **kwargs)
