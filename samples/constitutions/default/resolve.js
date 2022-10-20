export function resolve(proposal, proposerId, votes) {
  const memberVoteToAcceptCount = votes.filter((v) => v.vote).length;
  const memberVoteToRejectCount = votes.filter((v) => !v.vote).length;

  let activeMemberCount = 0;
  ccf.kv["public:ccf.gov.members.info"].forEach((v) => {
    const info = ccf.bufToJsonCompatible(v);
    if (info.status === "Active") {
      activeMemberCount++;
    }
  });

  // A majority of members can accept a proposal.
  if (memberVoteToAcceptCount > Math.floor(activeMemberCount / 2)) {
    return "Accepted";
  } else if (memberVoteToRejectCount > Math.floor(activeMemberCount / 2)) {
    return "Rejected";
  }

  return "Open";
}
