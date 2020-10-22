import pyReader from './utils/pyReader';
import { StockAction, StockInput, Stock, Portfolio  } from './types';
import { parseJSON } from './utils/parseUtils';
import { algorithmPath, profiles, stocks, performStockAction } from './dummyDataBase';
import { collapseTextChangeRangesAcrossMultipleVersions } from 'typescript';

// // TODO: Replace with real read and write methods
// const completeRound = (profileId: number, day: number, callback?: () => void) => {
//     const profile = profiles[profileId];
//     const currentStocks = stocks[day];
//     if (profile && currentStocks) {
//         const { algorithm, capital, portfolio = [] } = profile;
//         const input = [{capital, portfolio, stocks}];
//         const algorithmCallback = (result?: any[]) => {
//             if (result) {
//                 const actions = result.map(elem => parseJSON(elem) as StockAction);
//                 actions.forEach(action => performStockAction(profileId, action, day));
//                 callback?.()
//             }
//         };
//         pyReader.runScript(algorithmPath, algorithm, input, algorithmCallback);
//     } else {
//         !profile && console.log('found no profile with id: ' + profileId);
//         !currentStocks && console.log('found no stocks for day: ' + day);
//     }
// };

// export const performRounds = (profileId: number, startDay: number, days: number) => {
//     let currentDay = startDay;
//     const callback = () => {
//         if (currentDay < startDay + days) {
//             completeRound(profileId, currentDay, callback);
//         }
//         currentDay++;

//         console.log(profiles)
//     }
//     completeRound(profileId, currentDay, callback);
// };

// let a = pyReader.runScript('../stock_data', 'stock_data.py')


let myPort: Portfolio = {
    stocks: [1, 2],
    shares: [5,7],
};

let myStocks: Stock[] = 
    [{
        id: 1,
        name: 'first',
        value: [1,0,0],
    },
    {
        id: 2,
        name: 'second',
        value: [2,3,4],
    }];

let input: StockInput = {
    capital: 1,
    stocks: myStocks,
    portfolio: myPort,
};

// let input2 = [{capital, portfolio, stocks}];


// [JSON.stringify({"quantity": 2})]
pyReader.runScript('../algorithms', 'template_algorithm.py', input)
  