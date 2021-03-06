# Copyright 2014 0xc0170
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging

class Builder:
    """ Template to be subclassed """

    def build_project(self, project, project_path):
        raise NotImplementedError

    def build(self, projects_path, project_list, env_settings, root):
        # Loop through each of the projects and build them.
        logging.debug("Building projects.")

        for i, project_name in enumerate(project_list):
            logging.debug("Building project %i of %i: %s" %
                          (i + 1, len(project_list), project_name))
            self.build_project(project_name, projects_path[i], env_settings, root)
