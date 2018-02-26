# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2017 Mozilla Corporation

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../mq/plugins"))
from cloudtrail import message


class TestCloudtrailPlugin():
    def setup(self):
        self.plugin = message()

    def test_nonexistent_source(self):
        msg = {
            'category': 'someother',
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})
        assert retmessage == msg
        assert retmeta == {}

    def test_incorrect_source(self):
        msg = {
            'source': 'someother',
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})
        assert retmessage == msg
        assert retmeta == {}

    def test_iamInstanceProfile(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'iamInstanceProfile': 'astringvalue',
                }
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'iamInstanceProfile': {
                        'raw_value': 'astringvalue',
                    }
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_attribute(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'attribute': 'astringvalue',
                }
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'attribute': {
                        'raw_value': 'astringvalue',
                    }
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_description(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'description': 'astringvalue',
                }
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'description': {
                        'raw_value': 'astringvalue',
                    }
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_filter(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'filter': 'astringvalue',
                }
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'filter': {
                        'raw_value': 'astringvalue',
                    }
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_role(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'responseelements': {
                    'role': 'astringvalue',
                }
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'responseelements': {
                    'role': {
                        'raw_value': 'astringvalue',
                    }
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_additionaleventdata(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'additionaleventdata': 'astringvalue',
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'additionaleventdata': {
                    'raw_value': 'astringvalue',
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_serviceeventdetails(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'serviceeventdetails': 'astringvalue',
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'serviceeventdetails': {
                    'raw_value': 'astringvalue',
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_rule(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'rule': 'astringvalue',
                }
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'rule': {
                        'raw_value': 'astringvalue',
                    }
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_subnets(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'responseelements': {
                    'subnets': 'astringvalue',
                }
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'responseelements': {
                    'subnets': {
                        'raw_value': 'astringvalue',
                    }
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_endpoint(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'responseelements': {
                    'endpoint': 'astringvalue',
                }
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'responseelements': {
                    'endpoint': {
                        'raw_value': 'astringvalue',
                    }
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}

    def test_ebs_optimized(self):
        msg = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'ebsOptimized': 'astringvalue',
                }
            }
        }
        (retmessage, retmeta) = self.plugin.onMessage(msg, {})

        expected_message = {
            'source': 'cloudtrail',
            'details': {
                'requestparameters': {
                    'ebsOptimized': {
                        'raw_value': 'astringvalue',
                    }
                }
            }
        }
        assert retmessage == expected_message
        assert retmeta == {}
