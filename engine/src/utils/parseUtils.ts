export const parseJSON = (input: string): any => {
    const correctJson = input.replace(/(['"])?([a-z0-9A-Z_]+)(['"])?:/g, '"$2": ');
    return JSON.parse(correctJson);
}