package net.radzebra.itTalent.dao;

public class TalentTag {
    /**
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column talent_tag.talent_ID
     *
     * @mbggenerated Thu Sep 01 16:14:24 CST 2011
     */
    private String talentId;

    /**
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column talent_tag.tag_ID
     *
     * @mbggenerated Thu Sep 01 16:14:24 CST 2011
     */
    private String tagId;

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column talent_tag.talent_ID
     *
     * @return the value of talent_tag.talent_ID
     *
     * @mbggenerated Thu Sep 01 16:14:24 CST 2011
     */
    public String getTalentId() {
        return talentId;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column talent_tag.talent_ID
     *
     * @param talentId the value for talent_tag.talent_ID
     *
     * @mbggenerated Thu Sep 01 16:14:24 CST 2011
     */
    public void setTalentId(String talentId) {
        this.talentId = talentId == null ? null : talentId.trim();
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column talent_tag.tag_ID
     *
     * @return the value of talent_tag.tag_ID
     *
     * @mbggenerated Thu Sep 01 16:14:24 CST 2011
     */
    public String getTagId() {
        return tagId;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column talent_tag.tag_ID
     *
     * @param tagId the value for talent_tag.tag_ID
     *
     * @mbggenerated Thu Sep 01 16:14:24 CST 2011
     */
    public void setTagId(String tagId) {
        this.tagId = tagId == null ? null : tagId.trim();
    }
}