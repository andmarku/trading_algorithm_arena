import {PythonShell} from 'python-shell';
import { StockAction, StockInput, Stock, Portfolio  } from '../types';

const runScript = async (path: string, script: string, args: StockInput, callback?: ((results?: any[]) => void)) => {
    console.log(String("Printing the arguments to be sent to the Python script"))
    console.log('As json: \n' + String(JSON.stringify(args)) + '\n')
    
    // why does this not work??? not important but still
    // console.log('As string: \n' + JSON.parse(String(JSON.stringify(args)) + "\n"))

    const mode = 'text' as const;
    //const mode = 'json' as const;
    const options = {
        mode, 
        scriptPath: path,
        pythonOptions: ['-u'],
        args: [String(JSON.stringify(args))]
    };
    
    PythonShell.run(script, options, (err, results) => {
        if (err) throw err;
        if(results != null){
            console.log('returned results in pyshell as text: \n', results);
            console.log('returned results in pyshell as text: \n', results[0]);
            
            // parse to StockAction
            // let returnedJson = JSON.parse(results[0])
            // console.log('returned results in pyshell as json: \n', returnedJson);
            // console.log('returned results in pyshell: values in value array: \n', returnedJson['stocks'][0]['value']);

            // export type StockAction = {
            //     stockId: number,
            //     quantity: number,
            // };  
        }

        callback?.(results ?? []);
    }); 
}; 
  
export default {
    runScript,
};