import { Garden } from "./maps";

export const getGardensAround = async (
  ref: Garden,
  radius: number = 10
): Promise<Garden[]> => {
  try {
    const url = `http://localhost:3000/v1/products/vegetable?radius=${radius}`;
    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify({
        position: ref.position,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const results = await response.json();
    return results;
  } catch (e) {
    return [];
  }
};
