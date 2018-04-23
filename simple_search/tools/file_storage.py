
import os
import logging

from simple_search.tools.storage import Storage


logger = logging.getLogger(__name__)


class FileStorage(Storage):

    def __init__(self, index, config):
        super(FileStorage, self).__init__(index, config)
        self._storage_file_path = config.get('DATA_FILE_PATH')
        if not os.path.exists(os.path.dirname(self._storage_file_path)):
            os.makedirs(os.path.dirname(self._storage_file_path))
        open(self._storage_file_path, 'ab').close()

    def add(self, line: str):
        logger.debug('Adding new line')
        bin_data = line.encode('utf-8')
        len_data = len(bin_data)
        file_size = os.path.getsize(self._storage_file_path)

        with open(self._storage_file_path, 'ab') as storage_file:
            storage_file.write(bin_data)
            storage_file.write('|'.encode('utf-8'))

        for word in line.split(' '):
            if word:
                self._index.add(word.strip(), (file_size, len_data))

        return line

    def get_by_keyword(self, keys: str, limit: int=10):
        logger.debug('Search by keyword `%s`', keys)
        known_locations = []
        for key in keys.split():
            known_locations.append(self._index.get_by_key(key))

        matches = []
        if all([result.has_matches for result in known_locations]):
            base_match = set(known_locations[0].location)
            for result in known_locations:
                base_match = base_match.intersection(set(result.location))

            for location in base_match:
                with open(self._storage_file_path, 'rb') as storage_file:
                    storage_file.seek(location[0])
                    line = storage_file.read(location[1])
                    matches.append(line.decode('utf-8'))

                if len(matches) >= limit:
                    break

        return matches

    def reindexing(self):
        logger.info('Starting Reindexing existing data')
        byte_n = 0
        with open(self._storage_file_path, 'rb') as storage_file:
            for line in storage_file.read().split('|'.encode('utf-8')):
                if not line:
                    continue
                len_data = len(line)

                for word in line.decode('utf-8').split(' '):
                    if word:
                        self._index.add(word.strip(), (byte_n, len_data))

                byte_n += (len_data + 1)

        logger.info('Finished Reindexing existing data')
