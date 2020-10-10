import {PythonShell} from 'python-shell';

const runScript = async (path: string, script: string, args: any[] = [], callback?: ((results?: any[]) => void)) => {
    const mode = 'text' as const;
    const options = { mode, scriptPath: path, args };
    
    PythonShell.run(script, options, (err, results) => {
        if (err) throw err;
        console.log('results: ', results);
        callback?.(results ?? []);
    });
};

export default {
    runScript,
};