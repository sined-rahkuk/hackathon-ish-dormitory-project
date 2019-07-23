import json

class Configurator:
  
  def __init__(self, path='default_config.json'):
    self.conf_path = path
    self.config = None
    
  def read_configuration_from_file(self):
    try:
      config_file = open(self.conf_path, 'r', encoding='utf-8')
      self.config = json.load(config_file)
    except json.decoder.JSONDecodeError as e:
      print(e, ': not a valid config')
    except:
      print('something went wrong')
    finally:
      config_file.close()

  def get_configuration(self) -> dict:
    if self.config is not None:
      return self.config
    else:
      self.read_configuration_from_file()
      return self.config

  def save_configuration(self, config: dict) -> bool:
    if config is None:
      return False

    try:
      config_file = open(self.conf_path, 'w+', encoding='utf-8')
      json.dump(config, config_file)
    except:
      print('something went wrong')
    finally:
      config_file.close()
  

# config = Configurator().get_configuration()
# print(config)
