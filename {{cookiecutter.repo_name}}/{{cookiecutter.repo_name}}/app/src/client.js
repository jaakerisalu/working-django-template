import React from 'react';
import Iso from 'iso';
import * as Render from 'alt/utils/Render';

import Router from 'react-router';

import routes from './routes';
import alt from './alt';
import seo from './seo';
import logger from './logger';
import {i18n} from './i18n';


// Register to SEO store changes
seo();

// Run AltIso
Iso.on('iso', 1, function(state, meta, container) {
    alt.bootstrap(state);

    // Set correct language
    const activeLanguage = require('./stores/CurrentUserStore').getState().activeLanguage;
    logger.debug(`Set language to: ${activeLanguage}`);
    i18n.forceLanguage(activeLanguage);

    Router.run(routes, Router.HistoryLocation, (Handler, props) => {
        props.buffer = new Render.DispatchBuffer();
        React.render(<Handler {...props} />, container);
    });
});
