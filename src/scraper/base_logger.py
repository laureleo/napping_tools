import logging

lg = logging
lg.basicConfig(filename='output/events.log',
                    format='%(asctime)s %(message)s',
                    level=logging.INFO)
lg.getLogger().addHandler(logging.StreamHandler())
