import makeI18n, {setConfig, getConfig} from 'tg-i18n';

import logger from './logger';


setConfig('languageCode', DJ_CONST.LANGUAGE_CODE);
setConfig('localeData', DJ_CONST.LOCALE_DATA || {});
setConfig('logger', logger);

setConfig('onLanguageChange', theLanguage => {
    require('./actions/CurrentUserActions').changeLanguage(theLanguage);
});


const i18n = makeI18n();
export default i18n;
