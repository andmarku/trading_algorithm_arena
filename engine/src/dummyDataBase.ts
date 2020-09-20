import { Stock, StockAction, Portfolio } from './types';

let profiles: {[id: number]: {algorithm: string, capital: number, portfolio: Portfolio}} = {
    1: {
        algorithm: 'exampleAlgorithm1.py',
        capital: 150,
        portfolio: {},
    },
    2: {
        algorithm: 'exampleAlgorithm2.py',
        capital: 200,
        portfolio: {},
    }
};

const stocks: {[id: number]: Stock[]} = {
    0: [{id: 0, name: 'volvo', value: 24}, {id: 1, name: 'ikea', value: 34}, {id: 2, name: 'ericsson', value: 15}],
    1: [{id: 0, name: 'volvo', value: 25}, {id: 1, name: 'ikea', value: 32}, {id: 2, name: 'ericsson', value: 17}],
    2: [{id: 0, name: 'volvo', value: 27}, {id: 1, name: 'ikea', value: 33}, {id: 2, name: 'ericsson', value: 18}],
    3: [{id: 0, name: 'volvo', value: 29}, {id: 1, name: 'ikea', value: 32}, {id: 2, name: 'ericsson', value: 21}],
    4: [{id: 0, name: 'volvo', value: 26}, {id: 1, name: 'ikea', value: 28}, {id: 2, name: 'ericsson', value: 23}],
};

const algorithmPath = './';

const getUpdatedProfiles = (profileId: number, newCapital: number, newPortfolio: Portfolio) => ({
    ...profiles,
    [profileId]: { ...profiles[profileId], capital: newCapital, portfolio: newPortfolio },
});

const performStockAction = (profileId: number, action: StockAction, day: number) => {
    const profile = profiles[profileId];
    const currentStocks = stocks[day];
    if (profile && currentStocks) {
        const { portfolio = {}, capital = 0 } = profile;
        const stock = currentStocks.find(s => s.id === action.stockId);
        if (stock) {
            const { value } = stock;
            const maxAfforded = Math.floor(capital / value);
            const purchased = Math.min(maxAfforded, action.quantity);
            const cost = purchased * value;
            const newCapital = capital - cost;
            const newPortfolio = { ...portfolio, [stock.id]: (portfolio[stock.id] ?? 0) + purchased };
            profiles = getUpdatedProfiles(profileId, newCapital, newPortfolio);
        }
    }
};

export {
    profiles, stocks, performStockAction, algorithmPath,
}
