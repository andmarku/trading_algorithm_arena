export type Stock = {
    id: number,
    name: string,
    value: number[],
    available?: number,
};

export type Portfolio = {
    stocks: number[]
    shares: number[],
};

export type StockInput = {
    capital: number,
    stocks: Stock[],
    portfolio: Portfolio,
};

export type StockAction = {
    stockId: number,
    quantity: number,
    selling: boolean
};
