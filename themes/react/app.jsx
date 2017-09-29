const React = require('react');
import Index from './index';

class MutaleApp extends React.Component{
    render(){
        return (
            <div>
                <Index/>
            </div>
        )
    }
}


React.render(<MutaleApp/>, document.getElementById('magic_act'));