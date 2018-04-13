from simple_search.app import create_app


if __name__ == '__main__':
    app = create_app()

    port = app.config['API_PORT']
    app.logger.info('Starting Personity - API - %s', port)
    app.run(host=app.config['SERVER_HOST'], port=port)
    app.logger.info('Stopped Personity - API - %s', port)
