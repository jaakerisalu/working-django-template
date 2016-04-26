{% raw %}import React, {Component, PropTypes} from 'react';

import {gettext} from '../i18n';


class PageError extends Component {
    static propTypes = {
        pageFault: PropTypes.any.isRequired
    };

    render() {
        if (process.env.NODE_ENV !== 'production') {
            console.error('PageFault', this.props.pageFault, '-', this.props.pageFault.stack);
        }

        // TODO: Provide a nice error page
        // Warning: For production, we don't want to leak too much info here.
        return (
            <div className="container" style={{marginTop: '150px'}}>
                <div className="alert alert-danger">
                    <strong>{gettext('Oh snap!')}</strong> {gettext('Something went wrong.')}

                    <div>
                        <b>{gettext('Status Code:')}</b> {this.props.pageFault.statusCode}
                    </div>
                </div>

                <pre>{this.props.pageFault.responseText || this.props.pageFault}</pre>
            </div>
        );
    }
}

export default PageError;{% endraw %}
