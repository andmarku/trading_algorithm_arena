import pyReader from './utils/pyReader';
import { StockAction } from './types';
import { parseJSON } from './utils/parseUtils';
import { algorithmPath, profiles, stocks, performStockAction } from './dummyDataBase';

// TODO: Replace with real read and write methods
const completeRound = (profileId: number, day: number, callback?: () => void) => {
    const profile = profiles[profileId];
    const currentStocks = stocks[day];
    if (profile && currentStocks) {
        const { algorithm, capital, portfolio = [] } = profile;
        const input = [{capital, portfolio, stocks}];
        const algorithmCallback = (result?: any[]) => {
            if (result) {
                const actions = result.map(elem => parseJSON(elem) as StockAction);
                actions.forEach(action => performStockAction(profileId, action, day));
                callback?.()
            }
        };
        pyReader.runScript(algorithmPath, algorithm, input, algorithmCallback);
    } else {
        !profile && console.log('found no profile with id: ' + profileId);
        !currentStocks && console.log('found no stocks for day: ' + day);
    }
};

export const performRounds = (profileId: number, startDay: number, days: number) => {
    let currentDay = startDay;
    const callback = () => {
        if (currentDay < startDay + days) {
            completeRound(profileId, currentDay, callback);
        }
        currentDay++;

        console.log(profiles)
    }
    completeRound(profileId, currentDay, callback);
};

//performRounds(1,0,3)
pyReader.runScript('../', 'stock_data.py', [10, '2018-10-01'] )
