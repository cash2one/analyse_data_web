#!/usr/bin/env python
# encoding: utf-8

from analyse_data import app

if __name__=='__main__':
    app.logger.debug('## server started')
    app.run(debug=True)